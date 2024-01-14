class History:
    def __init__(self, potential_ini, adap_co_ini, position_ini, ligand_ini, receptor_ini):
        self.potential = [potential_ini]
        self.adap_co = [adap_co_ini]
        self.position = [position_ini]
        self.ligand = [ligand_ini]
        self.receptor = [receptor_ini]

    def update_potential(self, potential_new):
        self.potential.append(potential_new)

    def update_adap_co(self, adap_co_new):
        self.adap_co.append(adap_co_new)

    def update_position(self, adap_position_new):
        self.position.append(adap_position_new)

    def update_ligand(self, ligand_new):
        self.ligand.append(ligand_new)

    def update_receptor(self, receptor_new):
        self.receptor.append(receptor_new)
