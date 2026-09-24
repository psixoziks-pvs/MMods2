package ru.pnecrome;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/** Таблица всех известных науке скрещиваний (генерируется из tools/hybrids.txt). */
public class HybridRegistry {

    public interface Sink {
        void add(String id, String donor, String part, String ru, String en,
                 double hp, double sp, double dm, boolean fi, String desc);
    }

    private static final Map<String, List<HybridDef>> BY_DONOR_PART =
            new HashMap<String, List<HybridDef>>();
    private static final List<HybridDef> ALL = new ArrayList<HybridDef>();
    private static boolean loaded = false;

    private static class Gen implements Sink {
        @Override
        public void add(String id, String donor, String part, String ru, String en,
                        double hp, double sp, double dm, boolean fi, String desc) {
            HybridDef def = new HybridDef(id, "", part, donor, ru, en, hp, sp, dm, fi, desc);
            String k = donor + "|" + part;
            List<HybridDef> list = BY_DONOR_PART.get(k);
            if (list == null) {
                list = new ArrayList<HybridDef>();
                BY_DONOR_PART.put(k, list);
            }
            list.add(def);
            ALL.add(def);
        }
    }

    public static synchronized void init() {
        if (loaded) return;
        loaded = true;
        HybridTable.populate(new Gen());
    }

    /** Все подвиды, даваемые частью <code>part</code> от моба-донора <code>donorId</code>. */
    public static List<HybridDef> byDonorPart(String donorId, BodyPart part) {
        init();
        List<HybridDef> l = BY_DONOR_PART.get(donorId + "|" + part.key());
        return l == null ? new ArrayList<HybridDef>() : l;
    }

    /** Первый гибрид для пары (донор+часть), если он вообще существует. */
    public static HybridDef firstFor(String donorId, BodyPart part) {
        List<HybridDef> l = byDonorPart(donorId, part);
        return l.isEmpty() ? null : l.get(0);
    }

    public static List<HybridDef> all() {
        init();
        return ALL;
    }
}
