import os
import shutil
from datetime import datetime

def create_backup(source_path, backup_dir):
    """Crea una copia de seguridad del directorio fuente."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_filename = f"backup_{timestamp}.zip"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    shutil.make_archive(backup_path.replace('.zip', ''), 'zip', source_path)
    
    return backup_path
def restore_backup(backup_file, restore_dir):
    """Restaura la copia de seguridad en el directorio de destino."""
    if not os.path.exists(restore_dir):
        os.makedirs(restore_dir)
    
    shutil.unpack_archive(backup_file, restore_dir)
