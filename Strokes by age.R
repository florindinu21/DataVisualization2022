library(tidyverse)
library(ggplot2)
df<-read_csv("final_dataset.csv")

df1<-df[df[, "stroke"]==1, ]
df1 %>%
group_by(age) %>% 
summarize(total_strokes=sum(stroke)) %>%
ggplot(aes(x=age, y=total_strokes)) +
geom_bar(stat="identity", fill="steelblue")+
geom_text(aes(label=total_strokes), vjust=1.6, color="black", size=3)+
ggtitle("Total stroke cases by age") +
xlab("Age") + ylab("Total Strokes")+
theme(plot.title = element_text(hjust = 0.5), panel.background = element_blank())

