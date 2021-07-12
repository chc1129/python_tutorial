import shutil
shutil.copyfile('data.db', 'archive.dv')
shutil.move('/build/executables', installdir')
