package ru.pnecrome;

import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

/** Русские имена мобов-доноров для отображения частей тел. */
public class DonorNames {

    private static final Map<String, String> MAP = new HashMap<String, String>();

    static {
        MAP.put("axolotl", "аксолотля");
        MAP.put("bat", "летучей мыши");
        MAP.put("bee", "пчелы");
        MAP.put("blaze", "блаза");
        MAP.put("breeze", "бриза");
        MAP.put("camel", "верблюда");
        MAP.put("cat", "кошки");
        MAP.put("cave_spider", "пещерного паука");
        MAP.put("chicken", "курицы");
        MAP.put("cod", "трески");
        MAP.put("cow", "коровы");
        MAP.put("creeper", "крипера");
        MAP.put("dolphin", "дельфина");
        MAP.put("donkey", "осла");
        MAP.put("drowned", "утопленника");
        MAP.put("elder_guardian", "древнего стража");
        MAP.put("enderman", "эндермена");
        MAP.put("endermite", "эндермита");
        MAP.put("evoker", "заклинателя");
        MAP.put("fox", "лисы");
        MAP.put("frog", "лягушки");
        MAP.put("ghast", "гаста");
        MAP.put("giant", "гиганта");
        MAP.put("glow_squid", "светящегося кальмара");
        MAP.put("goat", "козла");
        MAP.put("guardian", "стража");
        MAP.put("hoglin", "хоглина");
        MAP.put("horse", "лошади");
        MAP.put("husk", "мумии");
        MAP.put("illusioner", "иллюзиониста");
        MAP.put("iron_golem", "железного голема");
        MAP.put("llama", "ламы");
        MAP.put("magma_cube", "магмового куба");
        MAP.put("mooshroom", "муушома");
        MAP.put("mule", "мула");
        MAP.put("ocelot", "оцелота");
        MAP.put("panda", "панды");
        MAP.put("parrot", "попугая");
        MAP.put("phantom", "фантома");
        MAP.put("pig", "свиньи");
        MAP.put("piglin", "пиглина");
        MAP.put("piglin_brute", "пиглина-брутала");
        MAP.put("pillager", "разбойника");
        MAP.put("polar_bear", "белого медведя");
        MAP.put("pufferfish", "рыбы-фугу");
        MAP.put("rabbit", "кролика");
        MAP.put("ravager", "разорителя");
        MAP.put("salmon", "лосося");
        MAP.put("sheep", "овцы");
        MAP.put("shulker", "шалкера");
        MAP.put("silverfish", "чешуйницы");
        MAP.put("skeleton", "скелета");
        MAP.put("slime", "слизня");
        MAP.put("sniffer", "нюхача");
        MAP.put("snow_golem", "снежного голема");
        MAP.put("spider", "паука");
        MAP.put("squid", "кальмара");
        MAP.put("stray", "снежного скелета");
        MAP.put("trader_llama", "торговой ламы");
        MAP.put("tropical_fish", "тропической рыбы");
        MAP.put("turtle", "черепахи");
        MAP.put("vex", "векса");
        MAP.put("villager", "жителя");
        MAP.put("vindicator", "ревнителя");
        MAP.put("warden", "наказателя");
        MAP.put("witch", "ведьмы");
        MAP.put("wither_skeleton", "иссушителя");
        MAP.put("wolf", "волка");
        MAP.put("zoglin", "зоглина");
        MAP.put("zombie", "зомби");
        MAP.put("zombie_villager", "зомби-жителя");
        MAP.put("zombified_piglin", "зомбифицированного пиглина");
    }

    public static String get(String fullId) {
        if (fullId == null) return "?";
        String s = fullId.toLowerCase(Locale.ROOT);
        int i = s.indexOf(':');
        if (i >= 0) s = s.substring(i + 1);
        String v = MAP.get(s);
        return v == null ? s : v;
    }
}
