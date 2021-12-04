class Tofu():
    volume = 777
    weight = 177
    texture = "Soft"

    def Tofu(self, water, soybeans, nigiri):
        print("Peparing to make some tofu. :))")
        soymilk = makeSoyMilk(water, soybeans)
        solution = beginCongelation(soymilk, nigiri)


        print("Made some tofu yo. :P")

    def makeSoyMilk(self, water, soybeans) -> object:
        return object;

    def beginCongelation(self, milk, nigiri) -> str:
        solution = object(str)
        for molecule_A in milk:
            for molecule_B in nigiri:
                if weight(solution) > 177:
                    return solution
                else:
                    solution += molecule_A + molecule_B

        return solution

    def __str__(self) -> str:
        return "Tofu made with bliss, peace and love."