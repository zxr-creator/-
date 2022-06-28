<template>
    <div id="line" style="height: 100%; width: 100%"></div>
  
</template>

<script>
import axios from 'axios'
import 'echarts' 
import VueEvent from '@/assets/utils/event'

export default {
  name: 'HelloWorld',
  data() {
      return {  
        linedata: [],
        before_box_office:[],
        after_box_office:[],
        new_cases:[]

      }
  },
  methods: {
      getdata(url) {
        axios.get(url)
          .then((res) => {
            this.linedata = res.data.linedata;
            console.log(this.linedata)
            for (var i = 0; i < this.linedata[0].new_cases.length; i++){
                this.before_box_office.push(this.linedata[0].before_box_office[i]);
                this.after_box_office.push(this.linedata[0].after_box_office[i]);
                this.new_cases.push(this.linedata[0].new_cases[i])
                }
          })
          .catch((error) => {
            console.log(error);
          })
      },

    drawLine(myLine){

        var that = this;
        var name = '全国';
        //图表的配置项和数据
        var option = {         
                title: {
                    text: '省区疫情前后每日电影票房及当日新增确诊人数',
                    textStyle: {
                        textSize:'20',
                        color:'#8ec06c'
                    },
                    left:'15%'
                },
                grid: {
                    x:"25%",
                    y:"30%",
                    x2:"7%",
                    y2:"5%"
                },
                xAxis: [
                    {
                        'type': 'category',//类目轴
                        'data': ['1日', '2日', '3日', '4日', '5日', '6日', '7日','8日', '9日', '10日', '11日', '12日', '13日', '14日','15日', '16日', '17日', '18日', '19日', '20日', '21日','22日', '23日', '24日', '25日', '26日','27日', '28日', '29日', '30日', '31日'],
                        axisPointer: {
                            type: 'shadow'
                        },
                        scale: true,            //脱离0值比例
                        boundaryGap: false,           // 折线紧挨边缘
                        // 字体设置
                        axisLabel:{
                            type:"solid",
                            color:"#56a0d3",
                            fontSize:"12",
                            nameLocation:'end'
                        },
                        // 坐标轴颜色
                        axisLine:{
                            color:'#56a0d3'
                        }
                    },
                ],
                yAxis: [
                    {
                        name:'当日票房',
                        nameTextStyle:{
                            type:"solid",
                            color:"#f77737",
                            fontSize:"14"
                        },
                        'type': 'value',//数值轴
                        min: 0,
                        interval: 100000000,
                        axisLabel: {
                            formatter: '{value}元',
                            type:"solid",
                            color:"#86888a",
                            fontSize:'14'
                        },
                    },
                    {
                        name:'当日新增确诊人数',
                        nameTextStyle:{
                            type:"solid",
                            color:"#f77737",
                            fontSize:"14"
                        },
                        'type': 'value',
                        min: 0,
                        interval: 1000,
                        axisLabel: {
                            formatter: '{value}人',
                            type:"solid",
                            color:"#fd1d1d"
                        }
                    }
                ],
                legend: [
                    {
                    data: ['疫情前每日票房', '疫情后每日票房', '当日新增确诊人数'],
                    right:10,
                    top:"10%",
                    textStyle:{
                        color:'#74d2e7',
                        fontSize:"14"
                    },
                },
            ],
            graphic: {
                type:'text',
                left: '22%',
                top: '12%',
                style:{
                    text: "当前区域："+ name,
                    font : 'bold 16px sans-serif',
                },
            },

                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                        type: 'cross',
                        crossStyle: {
                        color: '#999'
                        }
                    }
                },

                series: [
                    {name: '疫情前每日票房', type: 'bar',data: that.before_box_office},
                    {name: '疫情后每日票房', type: 'bar',data: that.after_box_office},
                    {name: '当日新增确诊人数', type: 'line',yAxisIndex: 1,data: that.new_cases}
                ]    
        }; 
 
        //使用刚指定的配置项和数据显示图表。
        setTimeout(()=>{
        option && myLine.setOption(option,true);
      },10)

      // 切换省区视图，获取CurrentIndex实现实时更新并渲染
        VueEvent.on('click',province =>{
            // 更新并载入省份数据
            var res = province.dataIndex
            //console.log(res)
            name = province.data.name
            console.log(name)
            var url = 'http://127.0.0.1:8002/api/getlinedata' + res;
            that.getdata(url)
        }),

        // 点击空白区域返回全国数据
        VueEvent.on('blank',function(){
            var url = 'http://127.0.0.1:8002/api/getlinedata';
            that.getdata(url)
            name = "全国"
        })

        VueEvent.on('timelinechanged',currentIndex =>{
            that.before_box_office = []
            that.after_box_office = []
            that.new_cases = [] 
            for (var i = 0; i < that.linedata[currentIndex].new_cases.length; i++){
                //console.log(i)
                that.before_box_office.push(that.linedata[currentIndex].before_box_office[i]);
                that.after_box_office.push(that.linedata[currentIndex].after_box_office[i]);
                that.new_cases.push(that.linedata[currentIndex].new_cases[i]);
            }
            setTimeout(()=>{
                myLine.setOption({
                    series:[
                        {name: '疫情前每日票房', type: 'bar',data: that.before_box_office},
                        {name: '疫情后每日票房', type: 'bar',data: that.after_box_office},
                        {name: '当日新增确诊人数', type: 'line',yAxisIndex: 1,data: that.new_cases}
                    ],
                    graphic: {
                        type:'text',
                        left: '22%',
                        top: '12%',
                        style:{
                            text: "当前区域："+ name,
                            font : 'bold 16px sans-serif',
                        },
                    }
                })
            },100) 
       }) 
    },
  },
  
    created(){
        var url = 'http://127.0.0.1:8002/api/getlinedata'
        this.getdata(url);
    },

    mounted(){
        var myLine = this.$echarts.init(document.getElementById('line'));
        this.drawLine(myLine);
  },
};


</script>

<style scoped>

</style>

