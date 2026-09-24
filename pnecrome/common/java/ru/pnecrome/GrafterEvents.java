package ru.pnecrome;

import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraftforge.event.entity.living.LivingDeathEvent;
import net.minecraftforge.event.entity.player.PlayerInteractEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;

public class GrafterEvents {

    /** Смерть моба -> он становится «трупом» на 2 минуты (не исчезает мгновенно). */
    @SubscribeEvent
    public void onDeath(LivingDeathEvent event) {
        LivingEntity e = event.getEntity();
        if (e.level.isClientSide) return;
        if (!(e instanceof Player) && !Necromancy.isCorpse(e)) {
            Necromancy.markCorpse(e);
        }
    }

    /** Правый клик частью тела по живому мобу -> скрещивание. */
    @SubscribeEvent
    public void onEntityInteract(PlayerInteractEvent.EntityInteract event) {
        Player player = event.getEntity();
        ItemStack held = event.getItemStack();
        if (!(event.getTarget() instanceof LivingEntity)) return;
        LivingEntity target = (LivingEntity) event.getTarget();
        if (!PartItems.isPart(held)) return;
        if (player.level.isClientSide) {
            event.setCanceled(true);
            event.setCancellationResult(InteractionResult.SUCCESS);
            return;
        }
        if (Necromancy.isCorpse(target)) {
            Messages.noCorpse(player);
            return;
        }
        if (Necromancy.graft(player.level, player, target, held)) {
            event.setCanceled(true);
            event.setCancellationResult(InteractionResult.SUCCESS);
        }
    }
}
