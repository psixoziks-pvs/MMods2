package ru.pnecrome;

/** Часть тела, которую можно выпилить из трупа и приживить другому мобу. */
public enum BodyPart {
    HEAD("head"), ARMS("arms"), LEGS("legs"), TORSO("torso");

    private final String key;

    BodyPart(String key) { this.key = key; }

    public String key() { return key; }

    public static BodyPart byKey(String key) {
        for (BodyPart p : values()) {
            if (p.key.equals(key)) return p;
        }
        return null;
    }

    public String ruName() {
        switch (this) {
            case HEAD: return "Голова";
            case ARMS: return "Руки";
            case LEGS: return "Ноги";
            default: return "Туловище";
        }
    }
}
