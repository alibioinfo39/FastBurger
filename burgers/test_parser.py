from fastq_parser import FastqParser

file_path = "test.fastq"  

parser = FastqParser(file_path)

for header, seq, qual in parser.parse(min_length=4, min_quality=9):
    print("Header:", header)
    print("Sequence:", seq)
    print("Quality:", qual)
    print("---")