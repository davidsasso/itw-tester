from DMM import Gdm834x


dmm = Gdm834x()

address = "ASRL3::INSTR"

dmm.open(address)

result = dmm.get_id()
print("Query Result:", result)


dmm.close()