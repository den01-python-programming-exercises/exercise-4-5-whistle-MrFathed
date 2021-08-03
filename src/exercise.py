from whistle import Whistle # imports

def main():
    #write your code below this line
    duck_whistle = Whistle("Kvaak")
    rooster_whistle = Whistle("Peef")

    print(duck_whistle.sound)
    print(rooster_whistle.sound)
    print(duck_whistle.sound)

if __name__ == '__main__':
    main()
