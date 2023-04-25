def agg(j):
    print((j['true_belief-reality-fact']+j['true_belief-second_order-mind']+j['true_belief-first_order-mind']+j['true_belief-memory-fact'])/673)
    print((j['second_order_false_belief-second_order-mind']+j['second_order_false_belief-first_order-mind']+j['second_order_false_belief-reality-fact']+j['second_order_false_belief-memory-fact'])/620)
    print((j['false_belief-second_order-mind']+j['false_belief-first_order-mind']+j['false_belief-reality-fact']+j['false_belief-memory-fact'])/568)
    print((j['true_belief-reality-fact']+j['false_belief-reality-fact']+j['second_order_false_belief-reality-fact'])/241)
    print((j['true_belief-second_order-mind']+j['false_belief-second_order-mind']+j['second_order_false_belief-second_order-mind'])/722)
    print((j['true_belief-first_order-mind']+j['false_belief-first_order-mind']+j['second_order_false_belief-first_order-mind'])/620)
    print((j['true_belief-memory-fact']+j['false_belief-memory-fact']+j['second_order_false_belief-memory-fact'])/278)

    print((j['true_belief-memory-fact']+j['false_belief-memory-fact']+j['second_order_false_belief-memory-fact']+j['true_belief-reality-fact']+j['false_belief-reality-fact']+j['second_order_false_belief-reality-fact'])/519)
    print((j['true_belief-first_order-mind']+j['false_belief-first_order-mind']+j['second_order_false_belief-first_order-mind']+j['true_belief-second_order-mind']+j['false_belief-second_order-mind']+j['second_order_false_belief-second_order-mind'])/1342)


li = ['zeroshot.json','fewshotsim2.json','fewshotsim4.json','fewshotsim8.json','fewshotsim16.json']
import json
for l in li:
    print('--------------------')
    j = json.load(open(l))
    agg(j['corrects'])
