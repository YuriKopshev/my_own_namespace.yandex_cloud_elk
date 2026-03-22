#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Create or update a text file on remote host

version_added: "1.0.0"

description: Create or update a text file at a given path with specified content.

options:
    path:
        description: The path (including filename) where the file will be created or modified.
        required: true
        type: str
    content:
        description: The content written to the file.
        required: true
        type: str
    backup:
        description:
            - Create a backup of the file if it exists.
        required: false
        type: bool
        default: false
author:
    - Yuri Kopshev
'''

EXAMPLES = r'''
# Create file
- name: Create file with content
  my_namespace.my_collection.my_own_module:
    path: /tmp/my_file.txt
    content: hello world

# Ensure file is updated
- name: Ensure file is updated
  my_namespace.my_collection.my_own_module:
    path: /tmp/my_file.txt
    content: new content
    backup: true
'''

RETURN = r'''
path:
    description: The path of the file.
    type: str
    returned: always
    sample: "/tmp/my_file.txt"
content:
    description: The content written to the file.
    type: str
    returned: always
    sample: "hello world"
changed:
    description: Whether the file was changed.
    type: bool
    returned: always
    sample: true
'''

from ansible.module_utils.basic import AnsibleModule
import os

def get_content(path):
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return f.read()

def run_module():
    # define arguments
    module_args = dict(
        path=dict(type="str", required=True),
        content=dict(type="str", required=True),
        backup=dict(type="bool", required=False, default=False),
    )

    result = dict(
        changed=False,
        path="",
        content="",
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    if module.check_mode:
        module.exit_json(**result)

    path = module.params["path"]
    want_content = module.params["content"]
    backup = module.params["backup"]

    result["path"] = path

    current_content = get_content(path)

    # если контент отличается или файла нет — меняем
    if current_content != want_content:
        result["changed"] = True

        if not module.check_mode:
            # при необходимости делаем бэкап
            if backup and current_content is not None:
                backup_path = path + ".backup"
                with open(backup_path, "w") as f:
                    f.write(current_content)

            # пишем новый контент
            with open(path, "w") as f:
                f.write(want_content)

    result["content"] = want_content

    module.exit_json(**result)


def main():
    run_module()


if __name__ == "__main__":
    main()
