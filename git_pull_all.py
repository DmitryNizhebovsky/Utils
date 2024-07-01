import os
import subprocess
import argparse

def git_pull_all(path='.'):
    for dirpath, dirnames, _ in os.walk(path):
        if '.git' in dirnames:
            print()
            os.chdir(dirpath)
            # Получаем текущую ветку
            current_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip().decode('utf-8')
            if current_branch == 'develop':
                # Проверяем наличие незакомиченных изменений
                status_output = subprocess.check_output(['git', 'status', '--porcelain']).strip()
                if status_output:
                    print(f'Skipping {dirpath}, there are uncommitted changes')
                else:
                    print(f'Pulling changes in {dirpath}')
                    result = subprocess.run(['git', 'pull'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if result.returncode == 0:
                        print(f'Successfully updated')
                    else:
                        print(f'Failed to update {dirpath}')
                        print(result.stderr.decode('utf-8'))
            else:
                print(f'Skipping {dirpath}, current branch is {current_branch}')
            os.chdir(path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update git repositories in a specified directory.')
    parser.add_argument('-d', '--directory', nargs='?', default='.', help='Directory to update repositories in (default: current directory)')
    
    args = parser.parse_args()
    git_pull_all(args.directory)