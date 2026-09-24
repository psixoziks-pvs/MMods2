package ru.pnecrome;

import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.player.Player;

public class Messages {
    public static void noCorpse(Player p) {
        p.displayClientMessage(Component.translatable("msg.pnecrome.no_corpse"), true);
    }

    public static void rejected(Player p) {
        p.displayClientMessage(Component.translatable("msg.pnecrome.reject"), true);
    }

    public static void grafted(Player p, Component name) {
        p.sendSystemMessage(Component.translatable("msg.pnecrome.grafted", name));
    }

    public static void sawn(Player p, Component name) {
        p.displayClientMessage(Component.translatable("msg.pnecrome.sawn", name), true);
    }
}
