import sys
import pprint as pp

from spark_optimizer.optimizer import calculate_spark_settings


def main(argv=None):
    if not argv:
        argv = sys.argv
    if len(argv) < 3 or len(argv) > 3:
        print("Two args are needed! (type, number nodes)")
        sys.exit(1)
    pp.pprint(calculate_spark_settings(argv[1], int(argv[2]))[0])
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv)
