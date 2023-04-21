class Runner:
    def __init__(self, ip: str, pubkey: bytes, privkey: bytes):
        self.ip = ip
        self.pubkey = pubkey
        self.privkey = privkey


# fmt: off
RUNNERS = {
    "ren": Runner(
        ip = "172.20.0.5",
        pubkey = bytes([30, 13, 213, 183, 143, 199, 186, 54, 69, 207, 12, 248, 233, 82, 135, 249, 169, 7, 245, 173, 162, 70, 59, 177, 25, 83, 175, 129, 16, 79, 254, 215]),
        privkey = bytes([8, 49, 72, 108, 96, 15, 187, 179, 176, 252, 174, 208, 7, 200, 74, 169, 165, 43, 189, 109, 180, 214, 69, 226, 40, 20, 177, 223, 170, 94, 200, 245]),
    ),
    "stimpy": Runner(
        ip = "172.20.0.15",
        pubkey = bytes([135, 116, 237, 121, 135, 72, 193, 101, 216, 29, 90, 29, 56, 216, 77, 82, 222, 68, 114, 72, 176, 230, 40, 109, 10, 250, 16, 74, 66, 253, 232, 169]),
        privkey = bytes([209, 25, 145, 151, 13, 182, 191, 63, 170, 198, 138, 92, 34, 72, 168, 92, 211, 143, 23, 116, 195, 81, 40, 234, 39, 116, 34, 229, 223, 69, 250, 113]),
    ),
    "george": Runner(
        ip = "172.20.0.25",
        pubkey = bytes([105, 195, 142, 134, 211, 61, 69, 152, 97, 239, 40, 220, 147, 241, 48, 10, 141, 115, 20, 18, 206, 146, 12, 8, 63, 254, 207, 63, 29, 203, 167, 145]),
        privkey = bytes([247, 144, 174, 132, 193, 157, 232, 153, 248, 122, 138, 186, 156, 122, 84, 187, 31, 58, 13, 62, 239, 93, 150, 9, 100, 173, 6, 104, 36, 160, 213, 206]),
    ),
}
# fmt: on
