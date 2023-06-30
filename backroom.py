def analyze_notebooks_for_readability():
    import nbformat
    from glob import glob
    from nbformat import read, write

    files = glob("*.ipynb")
    success_files = []
    failure_files = []

    for file in files:
        with open(file, 'r') as f:
            notebook = read(f, nbformat.NO_CONVERT)
        cells = [x for x in notebook['cells'] if x['cell_type'] == 'code']
        if len(cells) <= 1 or (len(cells) == 2 and cells[-1].source.strip() == ''):
            success_files.append(file)
        else:
            failure_files.append(file)
    action_needed_message = "Looks perfect." if len(failure_files) == 0 else """Action Needed\n==============\nFix the failures by combining the cells together.  The shortcut to do this is esc->shift+m.""" 
    failure_files_title = "" if len(failure_files) == 0 else """\n\nFailures\n========\n"""
    success_files = "\n".join(success_files)
    failure_files = "\n".join(failure_files)
    message = f"""\nSuccesses\n==========\n{success_files}{failure_files_title}{failure_files}\n\n{action_needed_message}
    """
    return message