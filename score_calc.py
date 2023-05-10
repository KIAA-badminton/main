def lim(x, uplim=20):
    '''将得分限制在0～uplim'''
    if x > uplim: return uplim
    if x < 0:  return 0
    return x

def get_score_1(p1_score, p2_score, p1_res, p2_res):
    '''
    # 用于计算KIAA羽毛球俱乐部积分赛的积分（单打）
    # 分数范围：0～100
    # rank = 分数 / 10
    # Parameters
        p1_score: 比赛前P1的分数
        p2_score: 比赛前P2的分数
        p1_res  : 对局中P1的得分
        p2_res  : 对局中P2的得分
    # Returns:
        p1_score_new: 比赛后P1的分数
        p2_score_new: 比赛后P2的分数
    '''
    
    def K(score):
        '''放大系数'''
        return 2 - 0.015 * score
    
    # 超过 20 分计为 20
    p1_res = lim(p1_res)
    p2_res = lim(p2_res)
    
    p1_exp = lim(20 + (p1_score - p2_score) / 2)  # P1的预期得分
    p2_exp = lim(20 - (p1_score - p2_score) / 2)  # P2的预期得分
    
    # 实际得分和预期的差
    dif = (p1_res - p1_exp) - (p2_res - p2_exp)
    print("预期比分: {:.1f} : {:.1f}".format(p1_exp, p2_exp))
    print("实际比分: {:.1f} : {:.1f}".format(p1_res, p2_res))
    
    p1_score_new = lim(p1_score + K(p1_score) * dif, 100)
    p2_score_new = lim(p2_score - K(p2_score) * dif, 100)
    print("赛后双方的分数变化：")
    print("P1: {:.1f} --> {:.1f}\nP2: {:.1f} --> {:.1f}".format(p1_score, p1_score_new,
                                                                p2_score, p2_score_new))
    return p1_score_new, p2_score_new


def get_score_2(t1_p1_score, t1_p2_score, t2_p1_score, t2_p2_score, t1_res, t2_res):
    '''
    # 用于计算双打积分
    # Parameters
        t1(2)_p1(2)_score: 比赛前Team1(2)中P1(2)的分数
        t1(2)_res  : 对局中Team1(2)的得分
    # Returns:
        t1(2)_p1(2)_score_new: 比赛后Team1(2)中P1(2)的分数
    '''
    t1 = (t1_p1_score + t1_p2_score) / 2
    t2 = (t2_p1_score + t2_p2_score) / 2
    t1_new, t2_new = get_score_1(t1, t2, t1_res, t2_res)
    
    t1_p1_score_new = lim( t1_p1_score + (t1_new - t1) / 2, 100)
    t1_p2_score_new = lim( t1_p2_score + (t1_new - t1) / 2, 100)
    t2_p1_score_new = lim( t2_p1_score + (t2_new - t2) / 2, 100)
    t2_p2_score_new = lim( t2_p2_score + (t2_new - t2) / 2, 100)
    
    return t1_p1_score_new, t1_p2_score_new, t2_p1_score_new, t2_p2_score_new
  
# get_score_1(60, 30, 21, 14)

# Output:
#   预期比分: 20.0 : 15.0
#   实际比分: 20.0 : 14.0
#   赛后双方的分数变化：
#   P1: 60.0 --> 61.1
#   P2: 50.0 --> 48.8
