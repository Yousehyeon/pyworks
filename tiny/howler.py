import argparse
import os
import sys

def get_args():
    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metaver='text',
                        type=str,
                        help='Input string or file')

# 외부 파일 처리 인자 추가
    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.txt).read().rstrip()

    return args

def main():
    args = get_args()
    # print(args.text)
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + '\n')
    out_fh.close()


if __name__=="__main__":
    main()