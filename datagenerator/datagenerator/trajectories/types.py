
def guess_trajectory_type(filepath):
    if "TRANSLATION" in filepath or "ROTATION" in filepath:
        return "computer_generated"
    elif "drone" in filepath or "fly" in filepath:
        return "drone"
    else:
        return "bird_flight"