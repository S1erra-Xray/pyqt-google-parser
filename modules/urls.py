from selenium.webdriver.support.ui import WebDriverWait

from .base import Base


class ParsingUrlsThread(Base):
    def run(self):
        self.status_bar.showMessage('Парсинг ссылок начат')
        self.lbl_progress.setText('Парсинг ссылок')

        try:
            with open(self.path, 'x') as f:
                x = 0
                max_val = self.sb_pages_count
                urls_count = 0
                self.progress_bar.setMaximum(max_val)
                while self.sb_pages_count != 0:
                    try:
                        is_captcha = self.driver.find_element(By.CSS_SELECTOR,
                                                              'body > div:nth-child(1) > div:nth-child(5) > b:nth-child(1)')
                        if is_captcha:
                            self.status_bar.showMessage('Решите капчу')
                    except:
                        print('капчи нет')

                    WebDriverWait(self.driver, 999999).until(EC.presence_of_element_located((By.ID, "result-stats")))

                    elements = self.driver.find_elements(By.CSS_SELECTOR, '.yuRUbf [href]')

                    for u in elements:
                        url = str(u.get_attribute('href'))
                        if 'webcache.googleusercontent.com' in url:
                            clear = url.split(':')[-2] + ':' + url.split(':')[-1].split('&')[0]
                        elif 'translate.google.com' in url:
                            clear = url.split('=')[-3].split('&')[0]
                        else:
                            clear = url

                        f.writelines(clear + '\n')
                        urls_count += 1

                    self.driver.find_element(By.CSS_SELECTOR, '#pnnext > span:nth-child(2)').click()
                    self.sb_pages_count -= 1
                    x += 1
                    self.progress_bar.setValue(x)

            self.driver.quit()
            self.status_bar.showMessage(f'Парсинг ссылок закончен. Найдено {urls_count}')
            self.progress_bar.setValue(max_val)

        except exceptions.NoSuchElementException:
            self.driver.quit()
            self.status_bar.showMessage(f'Парсинг завершен. Найдено {urls_count}')
            self.progress_bar.setValue(max_val)
            return

        except (exceptions.NoSuchWindowException, exceptions.WebDriverException):
            self.error_sig.emit('Браузер был закрыт', '')
            return
