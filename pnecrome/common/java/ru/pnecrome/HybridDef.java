package ru.pnecrome;

/** Подвид: базовый моб (жертва) + приживлённая часть донора => своё имя и статы. */
public class HybridDef {
    public final String id;
    public final String baseId;   // тип ЖЕРТВЫ ("minecraft:zombie")
    public final BodyPart part;   // какая часть приживлена
    public final String donorId;  // чья часть ("minecraft:creeper")
    public final String nameRu;
    public final String nameEn;
    public final double hpMul;
    public final double speedMul;
    public final double dmgMul;
    public final boolean fireImmune;
    public final String description;

    public HybridDef(String id, String baseId, String part, String donorId,
                     String nameRu, String nameEn,
                     double hpMul, double speedMul, double dmgMul,
                     boolean fireImmune, String description) {
        this.id = id;
        this.baseId = baseId;
        this.part = BodyPart.byKey(part);
        this.donorId = donorId;
        this.nameRu = nameRu;
        this.nameEn = nameEn;
        this.hpMul = hpMul;
        this.speedMul = speedMul;
        this.dmgMul = dmgMul;
        this.fireImmune = fireImmune;
        this.description = description;
    }

    /** Ключ гибридизации: какой моб + какая чужая часть. */
    public String key() {
        return baseId + "|" + part.key();
    }
}
