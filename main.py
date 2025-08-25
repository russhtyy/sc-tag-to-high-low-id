from math import floor

class PlayerTagConverter:
    """Converter between Clash-style Player Tags and High/Low IDs."""

    _alphabet = ["0", "2", "8", "9", "P", "Y", "L", "Q",
                 "G", "R", "J", "C", "U", "V"]  # Supercell's custom base-14 alphabet

    @classmethod
    def normalize_tag(cls, tag: str) -> str:
        """Normalize a tag (strip #, uppercase, replace O with 0)."""
        return tag.upper().replace("#", "").replace("O", "0")

    @classmethod
    def tag_to_id(cls, tag: str) -> tuple[int, int]:
        """Convert player tag -> (highID, lowID)."""
        tag = cls.normalize_tag(tag)
        total, i = 0, 0

        for ch in reversed(tag):
            total += cls._alphabet.index(ch) * (14 ** i)
            i += 1

        highID = total % 256
        lowID = floor(total / 256)
        return highID, lowID

    @classmethod
    def id_to_tag(cls, highID: int, lowID: int) -> str:
        """Convert (highID, lowID) -> player tag."""
        total = lowID * 256 + highID
        result = []

        while total > 0:
            result.append(cls._alphabet[total % 14])
            total //= 14

        return "#" + "".join(reversed(result))


if __name__ == "__main__":
    tag = input("\nWhat's the Player Tag?: #")

    highID, lowID = PlayerTagConverter.tag_to_id(tag)
    print(f"Tag {tag.upper()} -> High ID: {highID}, Low ID: {lowID}")

    restored_tag = PlayerTagConverter.id_to_tag(highID, lowID)
    print(f"Restored Tag from IDs -> {restored_tag}")
