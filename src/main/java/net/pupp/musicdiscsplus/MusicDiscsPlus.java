package net.pupp.musicdiscsplus;

import net.fabricmc.api.ModInitializer;
import net.pupp.musicdiscsplus.item.ItemGenerator;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import net.fabricmc.fabric.api.client.itemgroup.FabricItemGroupBuilder;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.util.Identifier;

public class MusicDiscsPlus implements ModInitializer {
	public static final String MOD_ID = "musicdiscsplus";
	public static final String MOD_NAME = "MusicDiscsPlus";
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

	@Override
	public void onInitialize() {
		ItemGenerator.registerItem();
	}

	public static final ItemGroup DISCS = FabricItemGroupBuilder.build(new Identifier(MOD_ID, "discs"), () ->
	{
		return new ItemStack(ItemGenerator.DISC_001);
	});
}
