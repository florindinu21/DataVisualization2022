
library(ggplot2)

df %>% 
  group_by(smoking_status,gender) %>% 
  mutate(freq = percent(sum(stroke) / nrow(df))) %>%
  ggplot(aes(x=smoking_status, y=freq,fill=gender)) +
  geom_bar(stat="identity", position="dodge")+
  geom_text(aes(label=freq), vjust=1.6, color="black", size=3)+
  ggtitle("Stroke rate per gender determined by smoking status") +
  xlab("Smoking_status") + ylab("Stroke rate")+
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1))+
  theme(plot.title = element_text(hjust = 0.5), panel.background = element_blank())
