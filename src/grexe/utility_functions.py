from typing import Tuple, List

from grexe.types import RebaseItem, OptionalFile


def get_files_modified(
    rebase_items: Tuple[RebaseItem, ...], include_files_excluded_by_user: bool = False
):
    file_changes: List[OptionalFile] = sum(
        [list(item.file_changes.values()) for item in rebase_items], start=[]
    )
    if not include_files_excluded_by_user:
        file_changes = [change for change in file_changes if change.included]
    files = [change.path for change in file_changes]
    return list(set(files))
