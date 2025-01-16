import requests

from .base import Base


class DownloadFilesThread(Base):
    def run(self):
        self.status_bar.showMessage('Загрузка файлов')
        self.lbl_progress.setText('Загрузка файлов')
        x = 0
        success = 0
        self.progress_bar.setMaximum(self.urls_count)
        with open(self.path, 'r') as f:
            for i in f:
                x += 1
                self.progress_bar.setValue(x)
                url = i.replace('\n', '')
                if self.is_downloadable(url=url):
                    r = requests.get(url, allow_redirects=True)
                    save_path = self.lne_folder_path.text() + '/' + self.get_filename_from_url(url)
                    try:
                        with open(save_path, 'xb') as f:
                            f.write(r.content)
                            success += 1
                    except OSError:
                        continue

        self.status_bar.showMessage(f'Успешно загружено {success} файлов')
