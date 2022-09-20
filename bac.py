def mention(oral, ecrit, maths, informatique):
    moyenne = (oral*2 + maths*4 + informatique*8 + ecrit*3)/17
    if moyenne < 10:
        return 'Recalé'
    elif moyenne < 12:
        return 'Sans mention'
    elif moyenne < 14:
        return 'Mention Assez Bien'
    elif moyenne < 16:
        return 'Mention Bien'
    elif moyenne >= 18:
        return 'Mention Tres Bien'

print(mention(15, 4, 19, 16))