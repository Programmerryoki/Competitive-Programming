class AqaAsadiNames:
    def getName(self,Dad,Mom,FirstChild,Gender):
        if Gender == "Boy":
            if FirstChild[0] not in "AEIOUY":
                return Dad.split()[0] + FirstChild.split()[1]
            else:
                return " ".join(Mom.split()[::-1])
        else:
            if FirstChild[0] not in "AEIOUY":
                return " ".join(Dad.split()[::-1])
            else:
                return Mom.split()[0] + FirstChild.split()[1]