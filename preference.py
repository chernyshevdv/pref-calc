import logging

def calculate_score(g_w, v_we, v_ws, g_e, v_es, v_ew, g_s, v_sw, v_se):
    """
    Gets three sets of Gora and Vists and calculates the final score returning three values.
    Returns a tuple of final score: W, E, S
    """
    logging.debug(f"calculate_score arguments: {locals()}")
    gora = [g_w, g_e, g_s]
    logging.debug(f"Parameters W: {(g_w, v_we, v_ws)}")
    logging.debug(f"Parameters E: {(g_e, v_es, v_ew)}")
    logging.debug(f"Parameters S: {(g_s, v_sw, v_se)}")

    amnister = min(gora)
    logging.debug(f"Amnister: {amnister}")
    gora_amnisted = list(map(lambda g: g - amnister, gora))
    logging.debug(f"Gora aminsted: {gora_amnisted}")
    gw_a, ge_a, gs_a = tuple(gora_amnisted)
    
    # Vists onto W:
    gw_in_vists = gw_a * 10 / 3
    v_ew += gw_in_vists
    v_sw += gw_in_vists
    logging.debug(f"Vists EW: {v_ew}")
    logging.debug(f"Vists SW: {v_sw}")

    # Vists onto E:
    ge_in_vists = ge_a * 10 / 3
    v_we += ge_in_vists
    v_se += ge_in_vists
    logging.debug(f"Vists WE: {v_we}")
    logging.debug(f"Vists SE: {v_se}")

    # Vists onto S:
    gs_in_vists = gs_a * 10 / 3
    v_es += gs_in_vists
    v_ws += gs_in_vists

    # Final vists
    v_final_s = v_se - v_es + v_sw - v_ws
    v_final_e = v_es - v_se + v_ew - v_we
    v_final_w = v_ws - v_sw + v_we - v_ew
    
    return v_final_w, v_final_e, v_final_s

if __name__ == "__main__":
    # Get player names:
    player_w = input("Name for WEST player: ")
    player_e = input("Name for EAST player: ")
    player_s = input("Name for SOUTH player: ")
    
    # Get figures for West
    print(f"{player_w} values:")
    g_w = int(input(f"Gora {player_w}: "))
    v_we = int(input(f"Vist {player_w} -> {player_e}: "))
    v_ws = int(input(f"Vist {player_w} -> {player_s}: "))

    # Get figures for East
    print(f"{player_e} values:")
    g_e = int(input(f"Gora {player_e}: "))
    v_ew = int(input(f"Vist {player_e} -> {player_w}: "))
    v_es = int(input(f"Vist {player_e} -> {player_s}: "))

    # Get figures for South
    print(f"{player_s} values:")
    g_s = int(input(f"Gora {player_s}: "))
    v_se = int(input(f"Vist {player_s} -> {player_e}: "))
    v_sw = int(input(f"Vist {player_s} -> {player_w}: "))

    # calculate final score:
    (score_w, score_e, score_s) = calculate_score(g_w, v_we, v_ws, g_e, v_es, v_ew, g_s, v_sw, v_se)

    # print out
    print("\nFINAL SCORE:")
    print(f"{player_w}: {score_w}")
    print(f"{player_e}: {score_e}")
    print(f"{player_s}: {score_s}")
