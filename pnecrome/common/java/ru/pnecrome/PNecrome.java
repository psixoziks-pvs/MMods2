package ru.pnecrome;

import net.minecraft.world.item.Item;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

/**
 * PNecrome — некромантский мод.
 * 1. Павший моб остаётся «трупом» ещё некоторое время — его можно распилить Костяной пилой.
 * 2. Части тел (голова / руки / ноги / туловище) приживляются любому живому мобу.
 * 3. Комбинация «тип жертвы + часть донора» даёт подвид со собственным именем (см. Некрономикон).
 */
@Mod(PNecrome.MODID)
public class PNecrome {

    public static final String MODID = "pnecrome";

    public static final DeferredRegister<Item> ITEMS =
            DeferredRegister.create(ForgeRegistries.ITEMS, MODID);

    public static final RegistryObject<Item> BONE_SAW = ITEMS.register("bone_saw",
            () -> new BoneSawItem(new Item.Properties().stacksTo(1)));

    public static final RegistryObject<Item> NECRONOMICON = ITEMS.register("necronomicon",
            () -> new NecronomiconItem(new Item.Properties().stacksTo(1)));

    public static final RegistryObject<Item> PART = ITEMS.register("part",
            () -> new PartItem(new Item.Properties()));

    public PNecrome() {
        IEventBus bus = FMLJavaModLoadingContext.get().getModEventBus();
        ITEMS.register(bus);
        HybridRegistry.init();
        bus.addListener(this::commonSetup);
        net.minecraftforge.common.MinecraftForge.EVENT_BUS.register(new GrafterEvents());
    }

    private void commonSetup(final FMLCommonSetupEvent event) {
    }
}
