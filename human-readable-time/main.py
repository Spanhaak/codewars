def make_readable(seconds):
    ''' transform seconds to HH:MM:SS format'''
    hours   = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    
    calculation = "%02i:%02i:%02i" % (hours, minutes, seconds)

    return calculation
