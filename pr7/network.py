from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print_doc(self, document):
        pass

class IScanner(ABC):
    @abstractmethod
    def scan_doc(self):
        pass

class ICopier(ABC):
    @abstractmethod
    def copy_doc(self):
        pass

class SimplePrinter(IPrinter):
    def print_doc(self, document):
        print(f"Друкую документ: {document}")

class SimpleScanner(IScanner):
    def scan_doc(self):
        print("Сканую документ...")
        return "сканований_документ.pdf"

class MFP(IPrinter, IScanner, ICopier):
    def print_doc(self, document):
        print(f"БФП: Друк: {document}")

    def scan_doc(self):
        print("БФП: Сканування...")
        return "скан_з_бфп.pdf"

    def copy_doc(self):
        doc_to_copy = self.scan_doc()
        self.print_doc(doc_to_copy)
        print("БФП: Копіювання завершено.")

printer = SimplePrinter()
scanner = SimpleScanner()
mfp = MFP()

printer.print_doc("Мій звіт.docx")

scanner.scan_doc()

mfp.copy_doc()
