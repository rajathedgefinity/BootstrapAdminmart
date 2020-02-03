from echarts import Echart, Legend, Bar, Axis

chart = Echart('Simple', 'Simple Data')
chart.use(Bar('INDIA',[2,3,4,5]))
chart.use(Legend(['Sampled Data']))
chart.use(Axis('category','bottom',data=['Nov','Dec','Jan','Feb']))
chart.plot()
