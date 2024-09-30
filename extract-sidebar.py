import os
import yaml

def get_sidebars_data(target_path):
    all_sidebars_data = []
    for dirpath, dirnames, filenames in os.walk(target_path):
        for file in filenames:
            if file == '_sidebar.yml':
                filepath = os.path.join(dirpath, file)
                with open(filepath, 'r') as sidebar_file:
                    sidebar_data = yaml.safe_load(sidebar_file)
                    all_sidebars_data.append(sidebar_data)
    return all_sidebars_data

def merge_yaml(merge_target_path, data_to_merge):
    with open(merge_target_path, 'r') as merge_target:
        merge_target_data = yaml.safe_load(merge_target)

    merge_target_data['website'].setdefault('sidebar', [])

    for sidebar in data_to_merge:
        merge_target_data['website']['sidebar'].append(sidebar)
    
    with open(merge_target_path, 'w') as output:
        yaml.dump(merge_target_data, output)

sidebars = get_sidebars_data('posts/')
merge_yaml('_quarto.yml', sidebars)