import paddle
try:
    from paddle.inference import Config
    print("Config imported successfully")
    cfg = Config()
    if hasattr(cfg, 'set_optimization_level'):
        print("set_optimization_level exists")
    else:
        print("set_optimization_level MISSING")
        
    # Also check AnalysisConfig directly if possible
    try:
        from paddle.base.libpaddle import AnalysisConfig
        ac = AnalysisConfig()
        if hasattr(ac, 'set_optimization_level'):
            print("AnalysisConfig.set_optimization_level exists")
        else:
            print("AnalysisConfig.set_optimization_level MISSING")
    except ImportError:
        print("Could not import AnalysisConfig directly")

except Exception as e:
    print(f"Error: {e}")
