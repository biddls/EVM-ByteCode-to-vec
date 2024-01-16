from src import CFG_reader


class Test_CFG_reader:
    path = "./src/ControlFlowGraphs/file.json"

    def test_parsedOpcodes(self):
        reader = CFG_reader.CFG_Reader(Test_CFG_reader.path)
        assert len(reader.parsedOpcodes) > 1

    def test_checkParsedOpcodes(self):
        reader = CFG_reader.CFG_Reader(Test_CFG_reader.path)
        assert len(reader.parsedOpcodes[0]) >= 1
        assert isinstance(reader.parsedOpcodes[0][0], str)
