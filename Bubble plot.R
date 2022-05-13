df1<- df[df[, "stroke"]==1, ]
df1
head(df1,10)


rownames(df1)

colnames(df1)

library(plotly)

df1$hypertension<-as.factor(df1$hypertension)

ggplot(head(df1,10), aes(x =rownames(head(df1,10)), y = smoking_status)) + 
  geom_point(aes(color = hypertension, size = age), alpha = 0.5) +
  scale_color_manual(values = c("#00AFBB", "#FC4E07")) + xlab("Sample")+
  scale_size(range = c(0.5, 12))


