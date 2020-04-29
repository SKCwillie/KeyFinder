key_list = [
    ['C maj', 'D min', 'E min', 'F maj', 'G maj', 'A min', 'B dim'],
    ['F maj', 'G min', 'A min', 'Bb maj', 'C maj', 'D min', 'E dim', 'A# maj'],
    ['G maj', 'A min', 'B min', 'C# maj', 'D maj', 'E min', 'F dim', 'Db maj'],
    ['Bb maj', 'C min', 'D min', 'Eb maj', 'F maj', 'G min', 'A dim', 'A# maj', 'D# maj'],
    ['D maj', 'E min', 'F# min', 'G maj', 'A maj', 'B min', 'C# dim', 'Gb min', 'Db dim'],
    ['Eb maj', 'F min', 'G min', 'Ab maj', 'Bb maj', 'C min', 'D dim', 'D# maj', 'G# maj', 'A# maj'],
    ['A maj', 'B min', 'C# min', 'D maj', 'E maj', 'F# min', 'G# dim', 'Db min', 'Gb min', 'Ab dim'],
    ['Ab maj', 'Bb min', 'C min', 'Db maj', 'Eb maj', 'F min', 'G dim', 'G# min', 'A# min', 'C# min', 'D# maj'],
    ['E maj', 'F# min', 'G# min', 'A maj' ,'B maj', 'C# min', 'D# dim', 'Gb min', 'Ab min', 'Db min', 'Eb dim'],
    ['Db maj', 'Eb min', 'F min', 'Gb maj', 'Ab maj', 'Bb min', 'C dim', 'C# maj', 'D# min', 'A# maj', 'G# maj', 'A# min'],
    ['B maj', 'C# min', 'D# min', 'E maj', 'F# maj', 'G# min', 'A# dim', 'Db min', 'Eb min', 'Gb min', 'Ab min', 'Bb dim'],
    ['F# maj', 'G# min', 'A# min', 'B maj', 'C# maj', 'D# min', 'E# dim', 'Gb maj', 'Ab min', 'Bb min', 'Db maj', 'Eb min', 'F dim']
]

def get_key(chord1, chord2):
    """Find possible key for two chords"""
    for key in key_list:
        if chord1 in key and chord2 in key:
            string = ("\n{}/{} is a possible key.\n".format(key[0], key[5]))
            print()
            print('='*(len(string)-1))
            print(string)
            print('='*(len(string)-1))
            print()
def menu_loop():
    """Show the menu."""
    root1 = input("\nWhat is the root of the first chord? ").upper().strip()
    third1 = input("\nIs the chord maj, min, or dim?  ").lower().strip()
    chord1 = root1 + ' ' + third1
    root2 = input("\nWhat is the root of the second chord?  ").upper().strip()
    third2 = input("\nIs the chord maj, min, or dim?  ").lower().strip()
    chord2 = root2 + ' ' + third2
    get_key(chord1, chord2)

if __name__ == '__main__':
    menu_loop()
