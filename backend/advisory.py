def get_advisory(disease):

    remedies = {
        "early_blight": "Spray chlorothalonil fungicide every 7 days.",
        "late_blight": "Use copper fungicide and remove infected leaves.",
        "leaf_mold": "Improve airflow and apply sulfur spray.",
        "healthy": "Crop healthy. Continue normal irrigation."
    }

    return remedies.get(disease, "Consult agriculture expert.")
