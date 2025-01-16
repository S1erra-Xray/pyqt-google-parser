from time import sleep

from .base import Base


class ParsingPhotosThread(Base):
    def run(self):
        self.status_bar.showMessage('Парсинг фотографий начат')
        self.lbl_progress.setText('Парсинг фотографий')

        self.driver.find_element(By.CSS_SELECTOR,
                                 "html body#gsr.srp div#main.main div#cnt.e9EfHf div#top_nav.gke0pe div#hdtb.GLcBOb div#pTwnEc.yg51vc div#hdtb-msb.IC1Ck div div.MUFPAc div.hdtb-mitem a").click()
        try:
            with open(self.path, 'x') as f:
                elements = self.driver.find_elements(By.CSS_SELECTOR, ".nfEiy")
                self.progress_bar.setMaximum(self.sb_pages_count)
                self.urls_count = 0
                for e in elements:
                    e.click()
                    sleep(5)
                    link = self.driver.find_element(By.CSS_SELECTOR,
                                                    "html body#yDmH0d.tQj5Y.ghyPEc.IqBfM.ecJEib.EWZcud.eejsDc.uirfo.notranslate.EIlDfe.cjGgHb.d8Etdd.LcUz9d.Wq3Ysf div.T1diZc.KWE8qe c-wiz.FA7L0b.P3Xfjc.SSPGKf.BIdYQ div.mJxzWe div#islsp.l39u4d div#Sva75c.WaWKOe.RfPPs div.A8mJGd div.dFMRD div.pxAole div.tvh9oe.BIB1wf c-wiz.Y6heUd div.nIWXKc div.OUZ5W div.zjoqD div.qdnLaf.isv-id div.v4dQwb a.eHAdSb img.n3VNCb").get_attribute(
                        "src")
                    f.writelines(link + '\n')
                    self.urls_count += 1
                    self.progress_bar.setValue(self.urls_count)
                    self.sb_count -= 1
                    if self.sb_count == 0:
                        break

                self.driver.quit()
                self.status_bar.showMessage('Парсинг фотографий закончен')

        except exceptions.NoSuchElementException as e:
            self.driver.quit()
            self.status_bar.showMessage('Парсинг завершен')
            return

        except (exceptions.NoSuchWindowException, exceptions.WebDriverException):
            self.error_sig.emit('Браузер был закрыт', '')
            return
