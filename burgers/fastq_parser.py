import gzip

class FastqParser:

    def __init__(self, file_path):
        self.file_path = file_path

    def _open_file(self):
        if self.file_path.endswith('.gz'):
            return gzip.open(self.file_path, 'rt')
        else:
            return open(self.file_path, 'r')

    def parse(self, min_length=0, min_quality=0):
        
        with self._open_file() as file:
            while True:
                header = file.readline().strip()
                if not header:
                    break 

                sequence = file.readline().strip()
                plus = file.readline().strip()
                quality = file.readline().strip()

                if not plus.startswith('+'):
                    raise ValueError(f"Expected '+' line, got: {plus}")
                if len(sequence) != len(quality):
                    raise ValueError(f"Sequence and quality lengths do not match for {header}")

                if len(sequence) < min_length:
                    continue

                if min_quality > 0:
                    phred_scores = [ord(q) - 33 for q in quality]
                    if min(phred_scores) < min_quality:
                        continue

                yield header, sequence, quality

    def __iter__(self):
        return self.parse() 