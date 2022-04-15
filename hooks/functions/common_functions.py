#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# maintainer (@johnsondnz)
"""
Common functions used by other modules
"""
import json
import subprocess
from logzero import logger

VLAN_MIN = 2
VLAN_MAX = 4094


def tag_cleanup(site_tags=None, skip=None) -> list:
    """
    Method cleans up the list of tags.
    params:
        site_tags: List of tags
    Return: list of unique tags
    """
    return [tag for tag in site_tags if skip is not None and tag not in skip]


def string_length(string: str, length: int, result=True) -> bool:
    """
    Checks the passed string is equal to or less than the passed in length.
    Returns: bool
    params:
        string: the string to test.
        length: the max length of the string.
    """
    return True if len(string) <= length else False


def message_logging(**kwargs) -> None:
    """
    Takes the inputs and print logging message to stdout
    params:
        kwargs:
            level: Indicated level (default = ERR)
            filename: Name of the file tested.
            message_title: Title of the message
            message: Message
            data: Any associated data that helps with identification
    Returns: None
    """

    level = kwargs.get("level") if "level" in kwargs else "ERR"
    filename = kwargs.get("filename")
    message_title = kwargs.get("message_title")
    message = kwargs.get("message")
    data = kwargs.get("data") if "data" in kwargs else None

    logger.error(f"[{level}] {filename} - {message_title}: {message}")
    if data is not None:
        logger.debug(f"[Error Data]: {data}")

    return None


def load_ansible_inventory(inventory_file=None) -> dict:
    """
    params:
      inventory_file: ini or yaml inventory file
    returns: Pythony dictionary
    """

    inventory = subprocess.run(
        [
            "ansible-inventory",
            "-i",
            inventory_file,
            "--list",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    inventory = json.loads(inventory.stdout.decode("utf-8"))
    return inventory
