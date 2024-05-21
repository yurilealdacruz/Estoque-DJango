import os
from datetime import datetime


dados = "mysqldump -u yakiro -h yakiro.mysql.pythonanywhere-services.com --set-gtid-purged=OFF --no-tablespaces 'yakiro$estoque'  > /home/yakiro/backupSQL/backup.sql"
# Nome do arquivo de backup com timestamp
backup_filename = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"

# Comando de backup
backup_command = f"mysqldump -u yakiro -h yakiro.mysql.pythonanywhere-services.com --set-gtid-purged=OFF --no-tablespaces 'yakiro$estoque'  > /home/yakiro/backupSQL/{backup_filename}"

# Executar o comando de backup
os.system(backup_command)