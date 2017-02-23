from sys import argv

print argv
print type(argv)

script, name, age = argv

print "Ciao %s. Hai %s anni" % (name, age)
