import sys
import printing


# Export functions

def export_answers(filename):
    sys.stdout = open(filename, "w")
    printing.print_all()

export_answers("game_stat_out.txt")
