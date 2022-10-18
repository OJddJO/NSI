def stat(txt: str):
    txt = txt.upper()
    dictionnary = {}
    for character in txt:
        if character.isupper():
            try:
                dictionnary[character] = dictionnary[character] + 1
            except:
                dictionnary[character] = 1
    return dictionnary

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse id auctor odio. Vestibulum lacus sem, vehicula id sollicitudin ac, eleifend in tellus. Duis tempor ligula enim, in vehicula orci lacinia sit amet. Aenean tincidunt sed tortor ut molestie. Nunc enim diam, pretium a est ac, vulputate auctor lectus. Vivamus pharetra, elit sit amet porta gravida, neque velit finibus dui, in volutpat eros ligula sit amet nulla. Fusce felis lorem, vestibulum at dapibus et, suscipit in nibh. Vivamus malesuada odio vitae eleifend blandit. Sed sit amet facilisis leo. Fusce varius ante a pharetra lacinia. Etiam sit amet nibh ut massa fermentum ornare. Donec mollis lobortis varius.

Mauris ullamcorper nisl et euismod tristique. Nunc blandit a ante non interdum. In nec suscipit tortor, quis scelerisque eros. Etiam accumsan iaculis enim vel feugiat. In magna quam, tempus a arcu sed, tristique rutrum nisl. Proin arcu lorem, interdum id leo quis, blandit ultricies neque. Nulla ultrices iaculis dictum. In hac habitasse platea dictumst. Praesent posuere nibh eu fermentum posuere. Aliquam ac interdum felis. Sed sed urna dignissim, sodales leo sit amet, convallis eros. Vestibulum pharetra mauris ut tempor lacinia. Nunc sit amet vestibulum dolor. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

Phasellus metus lectus, dictum ac molestie id, suscipit in est. Cras dictum cursus convallis. Donec sodales pharetra pulvinar. Mauris non massa nunc. Aliquam vehicula dignissim lorem, vel vestibulum ligula viverra vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean iaculis blandit nisl sed sollicitudin."""

print(stat(text))