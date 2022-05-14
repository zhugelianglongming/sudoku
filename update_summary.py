#!/usr/bin/env python3
import logging
import re
from pathlib import Path

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s",
                    datefmt="%m-%d %H:%M:%S")
log = logging.getLogger('summary')


class Catalog(object):
    """
    catalog in markdown
    """

    def __init__(self, path="SUMMARY.md"):
        """
        Create catalog
        :param path: path for catalog markdown
        """
        self.path = path
        log.debug("create catalog from {}".format(self.path))
        self.file = Path(path)
        self.content = self.file.read_text().splitlines()
        self.sub_catalogs = []

        # parse replaceable sub-catalog
        reg = re.compile('(?P<indent>.*)\\[comment\\]: <> \\((?P<path>.*) (?P<cmd>start|end)\\)')
        for idx, line in enumerate(self.content):
            match = reg.match(line)
            if match:
                log.debug("{}-{}-{}".format(match["indent"], match["path"], match["cmd"]))
                if match["cmd"] == "start":
                    sub_catalog = ReplacedSubCatalog(match["path"], match["indent"])
                    sub_catalog.set_start(idx)
                    self.sub_catalogs.append(sub_catalog)
                else:
                    # get last sub-catalog as corresponding start command
                    sub_catalog = self.sub_catalogs[-1]

                    # check corresponding start command
                    if sub_catalog.path != match["path"]:
                        raise AssertionError("command error: expect path[{}], not[{}]".format(
                            sub_catalog.path, match["path"]))
                    if sub_catalog.indent != match["indent"]:
                        raise AssertionError("command error: expect indent[{}], not[{}]".format(
                            sub_catalog.indent, match["indent"]))

                    # set end
                    sub_catalog.set_end(idx)

    def update_sub_catalog(self):
        """
        Update sub-catalog by command, and save in file
        replace content between below mark with content in related path:
            [comment]: <> ({path} start)
            [comment]: <> ({path} end)
        :return: updated content without title
        """
        cur = 0
        new_content = []
        reg = re.compile('(?P<prefix>.*\\])\\((?P<address>.*)\\)')
        for replaceable in self.sub_catalogs:
            # extend origin content before replaced sub-catalog
            new_content += self.content[cur:replaceable.start]

            # extend replaced sub-catalog content
            sub_catalog_file = Path(self.file.parent.joinpath(replaceable.path))
            sub_catalog = Catalog(sub_catalog_file)
            sub_catalog_content = sub_catalog.update_sub_catalog()
            print(sub_catalog_content)
            for line in sub_catalog_content:
                match = reg.match(line)
                if match:
                    # update relative address in link
                    new_address = Path(sub_catalog_file.parent.joinpath(match["address"]).relative_to(self.file.parent))
                    new_content.append("{}{}({})".format(replaceable.indent, match["prefix"], new_address))
                else:
                    new_content.append(replaceable.indent + line)

            cur = replaceable.end
        # extend origin content after all replaced sub-catalogs
        new_content += self.content[cur:]

        # save new content to file
        self.file.write_text(''.join('{}\n'.format(line) for line in new_content))
        return [line for line in new_content if is_useful_line(line)]  # pass command


def is_useful_line(line: str):
    """
    useless line includes:
        title
        command line and empty line before
    :param line:
    :return:
    """
    if line.startswith("#"):
        # title
        return False
    if not line.strip():
        # empty line
        return False
    if line.lstrip().startswith("["):
        # comment line
        return False
    return True


class ReplacedSubCatalog(object):
    """
    Sub-catalog to be replaced
    """

    def __init__(self, path, indent):
        """
        Create
        :param path: path for source content file
        :param indent: extra indent for replaced lines in Summary.md
        """
        self.path = path
        self.indent = indent
        self.start = None  # include
        self.end = None  # not include

    def set_start(self, start_cmd_idx):
        """
        Set start line for replaced content.
        It's the line right after start command line.
        :param start_cmd_idx: line number for start command
        :return:
        """
        self.start = start_cmd_idx + 1

    def set_end(self, end_cmd_idx):
        """
        Set end line for replaced content (which is not supposed to be replaced).
        It's the line right before end command line, it's empty line for markdown comment.
        :param end_cmd_idx: line number for end command
        :return:
        """
        self.end = end_cmd_idx - 1

    def __repr__(self):
        return "ReplacedSubCatalog(path: {}, start: {}, end: {}, indent: '{}')".format(
            self.path, self.start, self.end, self.indent)


if __name__ == '__main__':
    summary = Catalog()
    summary.update_sub_catalog()