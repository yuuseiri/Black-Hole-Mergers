print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\twhere there is none.
"""

print("------------")
print(poem)
print("------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars  = jelly_beans / 1000
    crates = jars / 100
    cargo_ships = crates / 10
    space_ships = cargo_ships / 4
    death_star = space_ships / 2
    return jelly_beans, jars, crates, cargo_ships, space_ships, death_star


start_point = 100000
beans, jars, crates, cargo_ships, space_ships, death_star = secret_formula(start_point)

print("With a starting point of: {}".format(start_point))

print(f"We'd have {beans} beans, {jars} jars, {crates} crates, {cargo_ships} cargo ships, {space_ships} space ships, and {death_star} death stars.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, {} crates, {} cargo ships, {} space ships, and {} death stars.".format(*formula))