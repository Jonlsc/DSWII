import os
import sys

# Adicione a pasta que contém o diretório 'coderflix' ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'coderflix'))

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  # Defina corretamente o módulo de configurações
    
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
